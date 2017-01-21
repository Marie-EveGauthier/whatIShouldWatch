<?php

namespace Tuto\TestBundle\Entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * films
 *
 * @ORM\Table()
 * @ORM\Entity(repositoryClass="Tuto\TestBundle\Entity\filmsRepository")
 */
class films
{
    /**
     * @var integer
     *
     * @ORM\Column(name="id", type="integer")
     * @ORM\Id
     * @ORM\GeneratedValue(strategy="AUTO")
     */
    private $id;

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
     * @ORM\Column(name="bechdel", type="integer")
     */
    private $bechdel;

    /**
     * @var integer
     *
     * @ORM\Column(name="dialogue_men", type="integer")
     */
    private $dialogueMen;

    /**
     * @var integer
     *
     * @ORM\Column(name="dialogue_women", type="integer")
     */
    private $dialogueWomen;


    /**
     * Get id
     *
     * @return integer
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set title
     *
     * @param string $title
     * @return films
     */
    public function setTitle($title)
    {
        $this->title = $title;

        return $this;
    }

    /**
     * Get title
     *
     * @return string
     */
    public function getTitle()
    {
        return $this->title;
    }

    /**
     * Set year
     *
     * @param integer $year
     * @return films
     */
    public function setYear($year)
    {
        $this->year = $year;

        return $this;
    }

    /**
     * Get year
     *
     * @return integer
     */
    public function getYear()
    {
        return $this->year;
    }

    /**
     * Set bechdel
     *
     * @param integer $bechdel
     * @return films
     */
    public function setBechdel($bechdel)
    {
        $this->bechdel = $bechdel;

        return $this;
    }

    /**
     * Get bechdel
     *
     * @return integer
     */
    public function getBechdel()
    {
        return $this->bechdel;
    }

    /**
     * Set dialogueMen
     *
     * @param integer $dialogueMen
     * @return films
     */
    public function setDialogueMen($dialogueMen)
    {
        $this->dialogueMen = $dialogueMen;

        return $this;
    }

    /**
     * Get dialogueMen
     *
     * @return integer
     */
    public function getDialogueMen()
    {
        return $this->dialogueMen;
    }

    /**
     * Set dialogueWomen
     *
     * @param integer $dialogueWomen
     * @return films
     */
    public function setDialogueWomen($dialogueWomen)
    {
        $this->dialogueWomen = $dialogueWomen;

        return $this;
    }

    /**
     * Get dialogueWomen
     *
     * @return integer
     */
    public function getDialogueWomen()
    {
        return $this->dialogueWomen;
    }
}
