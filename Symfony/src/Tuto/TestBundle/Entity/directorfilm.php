<?php

namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * directorfilm
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\directorfilmRepository")
 */
class directorfilm {

    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

    /**
      /**
     * @ORM\ManyToOne(targetEntity="Directors", inversedBy="id")
     * @ORM\JoinColumn(name="director_id", referencedColumnName="id")

     */
    private $directorId;

    /**
     * @ORM\ManyToOne(targetEntity="Films", inversedBy="id")
     * @ORM\JoinColumn(name="film_id", referencedColumnName="id")
     */
    private $filmId;

    /**
     * Get id
     *
     * @return integer
     */
    public function getId() {
        return $this->id;
    }

    /**
     * Set directorId
     *
     * @param integer $directorId
     * @return directorfilm
     */
    public function setDirectorId($directorId) {
        $this->directorId = $directorId;

        return $this;
    }

    /**
     * Get directorId
     *
     * @return integer
     */
    public function getDirectorId() {
        return $this->directorId;
    }

    /**
     * Set filmId
     *
     * @param integer $filmId
     * @return directorfilm
     */
    public function setFilmId($filmId) {
        $this->filmId = $filmId;

        return $this;
    }

    /**
     * Get filmId
     *
     * @return integer
     */
    public function getFilmId() {
        return $this->filmId;
    }

}
