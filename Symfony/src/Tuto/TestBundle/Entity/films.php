<?php


namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;
use Doctrine\Common\Collections\ArrayCollection;

/**
 * films
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\filmsRepository")
 */
class films {

    /**


     * @ORM\Id
     * @ORM\Column(type="integer")
     * @ORM\GeneratedValue(strategy="AUTO")
     * @ORM\OneToMany(targetEntity="writerfilm", mappedBy="idFilm")

     */
    private $id;

    /** public function __construct() {
      $this->film = new ArrayCollection();
      }
     */
    /**


     */

    /**
     * @var string
     *
     * @ORM\Column(name="title", type="string", length=255)
     */
    private $title;

    /**
     * @var integer
     *
     * @ORM\Column(name="year", type="integer")
     */
    private $year;

    /**
     * @var integer
     *
     * @ORM\Column(name="bechdel", type="integer",nullable=true)
     */
    private $bechdel = NULL;

    /**
     * @var float
     *
     * @ORM\Column(name="dialogue_men", type="float",nullable=true)
     */
    private $dialogueMen = NULL;

    /**
     * @var float
     *
     * @ORM\Column(name="dialogue_women", type="float",nullable=true)
     */
    private $dialogueWomen = NULL;

    /**
     * @var string
     *
     * @ORM\Column(name="imdb_id", type="string",nullable=true)
     */
    private $imdb_id = NULL;

    /**
     * @var string
     *
     * @ORM\Column(name="image_url", type="string",nullable=true)
     */
    private $image_url = NULL;

    /**
     * Get id
     *
     * @return integer
     */
    public function getId() {
        return $this->id;
    }

    /**
     * Set title
     *
     * @param string $title
     * @return films
     */
    public function setTitle($title) {
        $this->title = $title;

        return $this;
    }

    /**
     * Get title
     *
     * @return string
     */
    public function getTitle() {
        return $this->title;
    }

    /**
     * Set year
     *
     * @param integer $year
     * @return films
     */
    public function setYear($year) {
        $this->year = $year;

        return $this;
    }

    /**
     * Get year
     *
     * @return integer
     */
    public function getYear() {
        return $this->year;
    }

    /**
     * Set bechdel
     *
     * @param integer $bechdel
     * @return films
     */
    public function setBechdel($bechdel) {
        $this->bechdel = $bechdel;

        return $this;
    }

    /**
     * Get bechdel
     *
     * @return integer
     */
    public function getBechdel() {
        return $this->bechdel;
    }

    /**
     * Set dialogueMen
     *
     * @param integer $dialogueMen
     * @return films
     */
    public function setDialogueMen($dialogueMen) {
        $this->dialogueMen = $dialogueMen;

        return $this;
    }

    /**
     * Get dialogueMen
     *
     * @return integer
     */
    public function getDialogueMen() {
        return $this->dialogueMen;
    }

    /**
     * Set dialogueWomen
     *
     * @param integer $dialogueWomen
     * @return films
     */
    public function setDialogueWomen($dialogueWomen) {
        $this->dialogueWomen = $dialogueWomen;

        return $this;
    }

    /**
     * Get dialogueWomen
     *
     * @return integer
     */
    public function getDialogueWomen() {
        return $this->dialogueWomen;
    }

    /**
     * Set imdb_id
     *
     * @param string $imdbId
     * @return films
     */
    public function setImdbId($imdbId) {
        $this->imdb_id = $imdbId;

        return $this;
    }

    /**
     * Get imdb_id
     *
     * @return string
     */
    public function getImdbId() {
        return $this->imdb_id;
    }

    /**
     * Set image_url
     *
     * @param string $imageUrl
     * @return films
     */
    public function setImageUrl($imageUrl) {
        $this->image_url = $imageUrl;

        return $this;
    }

    /**
     * Get image_url
     *
     * @return string
     */
    public function getImageUrl() {
        return $this->image_url;
    }

    /**
     * Set film
     *
     * @param \Tuto\TestBundle\Entity\writerfilm $film
     * @return films
     */
    public function setFilm(\Tuto\TestBundle\Entity\writerfilm $film = null) {
        $this->film = $film;

        return $this;
    }

    /**
     * Get film
     *
     * @return \Tuto\TestBundle\Entity\writerfilm
     */
    public function getFilm() {
        return $this->film;
    }

    /**
     * Set writer
     *
     * @param integer $writer
     * @return films
     */
    public function setWriter($writer) {
        $this->writer = $writer;

        return $this;
    }

    /**
     * Get writer
     *
     * @return integer
     */
    public function getWriter() {
        return $this->writer;
    }

}
